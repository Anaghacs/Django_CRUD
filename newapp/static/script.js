function validate(){
    console.log("hi")
    var first_name = document.getElementsByClassName('input1');
    var last_name=document.getElementsByClassName('input1');
    var email=document.getElementsByClassName('input2');
    var phone=document.getElementsByClassName('input2');
    var place=document.getElementsByClassName('input2');

    if(first_name==""||first_name===" "||last_name==""||last_name===" "||place==""||place===" ")
    {
        document.getElementById('username-error').innerHTML="Please enter valid detals";
        document.getElementById('username-error').style.display="block";
    }
    var re = "/^[a-z0-9+_.-]+@[a-z0-9.-]+$"
    var x=re.test(email);
    if(x)
    {}
    else
    {
        document.getElementById('username-error').innerHTML="Please enter valid email address valid item"
        document.getElementById('username-error').style.display="block";
    }   
    var check="^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$"
    var a=check.test(phone);
    if(a)
    {}
    else
    {
        document.getElementById('username-error').innerHTML="Please enter 10 digit phone number"
        document.getElementById('username-error').style.display="block";
    }             
    document.getElementById('username-error').style.display="none";
    
}