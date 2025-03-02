
document.getElementById("submit-btn").addEventListener('click', sendDataToPython )

async function sendDataToPython(){

    const user = document.getElementById("user-input").value
    const passwd = document.getElementById("password-input").value

    data = {"username" : user, "password" : passwd}

    dataPacket = {
        method : "POST",
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify(data),
        credentials : 'include'


    }

    console.log(dataPacket)

    const response = await fetch("http://127.0.0.1:5000/validate_credentials", dataPacket)
    const respData = await response.json()
    const dispFlag = respData.flag  

    if(dispFlag=='1'){
        document.getElementById('failure-message').style.display = "none"
        document.getElementById('dne-message').style.display = "none"
        document.getElementById('success-message').style.display = "inline"
        window.location.href = "http://127.0.0.1:5000/"
    }
    if(dispFlag=='0'){
        
        document.getElementById('success-message').style.display = "none"
        document.getElementById('dne-message').style.display = "none"
        document.getElementById('failure-message').style.display = "inline"
    }

    if(dispFlag=='2'){
        
        document.getElementById('success-message').style.display = "none"
        
        document.getElementById('failure-message').style.display = "none"
        document.getElementById('dne-message').style.display = "inline"
    }

    

    console.log(respData.message)


}