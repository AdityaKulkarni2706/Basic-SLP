document.getElementById('cred-btn').addEventListener('click', sendDataToApp)

async function sendDataToApp(){
    const username = document.getElementById("username-input").value
    const password = document.getElementById("password-input").value
    const data = {"username": username, "password" : password}

    console.log(username)
    console.log(password)

    const insertRequest_With_Data_Combined = {
        method : "POST",
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify(data),
        credentials : 'include'
        

    }

    const response = await fetch("http://localhost:5000/insert_data_into_DB", insertRequest_With_Data_Combined)
    const responseData = await response.json()
    const display_flag = responseData.flag
    console.log(responseData)
    

    if(display_flag=='1'){
        document.getElementById('failure-message').style.display = "none"
        document.getElementById('success-message').style.display = "inline"
        
    }
    if(display_flag=='0'){
        
        document.getElementById('success-message').style.display = "none"
        document.getElementById('failure-message').style.display = "inline"
    }

    console.log(responseData.message)






}