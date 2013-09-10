//////////////////////////////////////////////////////////////////////
// JS Form Validation Library
// by Jonas Gorauskas
// Created: 2007-07-09 10:22:05
// 
// History:
//   
//   2007-07-09 10:22:31 - JGG
//     Initial Version
//////////////////////////////////////////////////////////////////////


function confirmSubmission(msg) {
    return (confirm(msg));
}


function isEmpty(formField, msg) {
    with (formField) {
        if (value.length == 0) {
            alert(msg);
            return true;
        } else {
            return false;
        }
    }
}


function isEmail(formField, msg) {
    var emailRegEx = "^[\\w-_\.]*[\\w-_\.]\@[\\w]\.+[\\w]+[\\w]$";
    var regEx = new RegExp(emailRegEx);

    if (regEx.test(formField.value)) {
        return true;
    } else {
        alert(msg);
        return false;
    }
}


function isNumber(formField, msg) {
    if (isEmpty(formField, msg)) {
        return false;
    }

    var i = parseInt(formField.value);

    if (isNaN(i)) {
        alert(msg);
        return true;
    } else {
        return true;
    }
}


function isFloat(formField, msg) {
    if (isEmpty(formField, msg)) {
        return false;
    }

    var i = parseFloat(formField.value);

    if (isNaN(i)) {
        alert(msg);
        return true;
    } else {
        return true;
    }
}


function isAlpha(formField, msg) {
    //Alpha characters only - no Numbers allowed
}


function isAlphaNumeric(formField, msg) {
    //all alphanumeric caracthers are valid - no special characters allowed
    //ranges from [A-Z] [a-z] [0-9]
}


function isPasswordStrong(formField, msg) {
    //check password strength based on regex
    // length >= 8
    // at least one upper case character
    // at least one special character (upper ASCII code)
}


function isPasswordIdentical(formField1, formField2, msg) {
    if (formField1.value == formField2.value) {
        return true;
    }  else {
        alert(msg);
        return false;
    }
}


function isNumberInRange(formField, minVal, maxVal, msg) {
    if (isNumber(formField, msg)) {
        return false;
    }

    var i = parseInt(formField.value); //error trap

    if ((i < minVal) || (i > maxVal)) {
        alert(msg);
        return false;
    } else {
        return true;
    }
}


function isAlphaInRange() {
    //checks if an alphanumeric value falls within a range of values
}


