using System;
using System.Collections.Generic;

public class MyClass
{
	public static void Main()
	{
		foreach (long l in GetCounter(0, 20, 3)) {
			WL(l.ToString());
		}
		
		RL();
	}
	
	public static IEnumerable<long> GetCounter(long init, long end, long step) {
		for (long l = init; l <= end; l += step) {
			yield return l;
		}
	}
	
	#region Helper methods

	private static void WL(object text, params object[] args)
	{
		Console.WriteLine(text.ToString(), args);	
	}
	
	private static void RL()
	{
		Console.ReadLine();	
	}
	
	private static void Break() 
	{
		System.Diagnostics.Debugger.Break();
	}

	#endregion
}