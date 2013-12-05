<#
.SYNOPSIS
    Simple script to produce a listing of user's group memberships
.DESCRIPTION
    Script will create a simple listing of a user's group memberships.
    Output is in object format so you can use other Powershell cmdlet's
    with the output, such as Export-CSV, Out-File, ConvertTo-HTML, etc.
    
    Groups are presented using the friendly name, and are sorted
    alphabetically.
.PARAMETER User
    Name of the user you want to list
.INPUTS
    Pipeline
    Get-ADUser    
.OUTPUTS
    PSObject    User Name
                Group Name
.EXAMPLE
    .\Get-UserGroupMembership.ps1 -User username
    List all of the groups for "username"
.NOTES
    Author:            Jonas Gorauskas  
    Email              jonas_gorauskas@intuit.com
       
    Changelog:
       1.0             Initial Release
#>

Param (
    [Parameter(Mandatory=$true,ValueFromPipeLine=$true)]
    [Alias("ID","Users","Name")]
    [string[]]$User
)
Begin {
    Try { Import-Module ActiveDirectory -ErrorAction Stop }
    Catch { Write-Host "Unable to load Active Directory module, is RSAT installed?"; Break }
}

Process {
    ForEach ($U in $User) {
        $UN = Get-ADUser $U -Properties MemberOf
        $Groups = ForEach ($Group in ($UN.MemberOf)) {   
            #(Get-ADGroup $Group).SamAccountName
            Get-ADGroup $Group
        }

        $Groups = $Groups | Sort

        ForEach ($Group in $Groups) {
            New-Object PSObject -Property @{
                #Name = $UN.Name
                Name = $Group.SamAccountName;
                Group = $Group;
                Scope = $Group.GroupScope;
            }
        }
    }
}
