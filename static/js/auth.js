document.getElementById("sidebarCollapse").addEventListener("click", function () {
    document.querySelector(".aside").classList.toggle("aside_collapsed");
});

function initGSignInLibrary() {
    const scopes = 'profile email';
    const clientId = '652133526103-0au47p0qtlfe5frrtggvojohv79hcvmu.apps.googleusercontent.com';
    // const apiKey = 'AIzaSyBCawh2etNJZTS3G9t0K1O6y-MNQeK5xoY';
    const signinButton = document.querySelector("#signinButton");
    const signoutButton = document.getElementById("signoutButton");
    // const createRequestForm = document.forms['createRequestForm'];
    const pathname = window.location.pathname;
    //Load the API client and auth2 library
    gapi.load('auth2', function () {
        gapi.auth2.init({
            // apiKey: apiKey,
            // client_id: clientId,
            // scope: scopes
        }).then(function (auth2) {
            // Listen for sign-in state changes.
            // gapi.auth2.getAuthInstance().isSignedIn.listen(updateSigninStatus);
            // Handle the initial sign-in state.
            // updateSigninStatus(gapi.auth2.getAuthInstance().isSignedIn.get());
            // auth2.attachClickHandler('signinButton', {
            //     prompt: "select_account",
            // }, onSignIn, onSignInFailure);

            // function onSignIn(googleUser) {
            //     const id_token = googleUser.getAuthResponse().id_token;
            //     console.log(pathname);
            //     sendServerRequest(pathname, {id_token: id_token});
            // }
            // function onSignInFailure(error){
            //     console.log(error);
            // }
            if(signinButton) {
                signinButton.addEventListener("click", function (event) {
                    console.log(pathname);
                    auth2.grantOfflineAccess().then(function (authResult) {
                        if (authResult['code']) {
                            sendServerRequest(pathname, {auth_code: authResult['code']});
                        }
                        else {
                            console.log('Cannot find auth code')
                        }
                    });
                });
            }

            if (signoutButton) {
                signoutButton.addEventListener("click", function (event) {
                    // gapi.auth2.getAuthInstance().signOut();
                    console.log(pathname);
                    sendServerRequest(pathname, {});
                });
            }
        });
    });


    // function updateSigninStatus(isSignedIn) {
    //     console.log(isSignedIn);
    //     if (isSignedIn) {
    //         // User is signed in.
    //         // Pass currentUser to onSignIn callback.
    //         console.log("signed in");
    //     } else {
    //         console.log("not signed in");
    //     }
    // }

    // function sendServerRequest(url, data) {
    //     console.log("Prepare to request");
    //     var xhr = new XMLHttpRequest();
    //     xhr.open('POST', url);
    //     var csrftoken = getCookie('csrftoken');
    //     xhr.setRequestHeader('X-CSRFToken', csrftoken);
    //     xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
    //     xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    //     xhr.withCredentials = true;
    //     xhr.onreadystatechange = function() {
    //         if (this.readyState === 4 && this.status === 200) {
    //             //window.location.href = 'REDIRECT_URL'
    //             console.log(xhr.statusText);
    //             window.location.reload();
    //         }
    //     };
    //     // xhr.onload = function() {
    //     //     console.log(xhr.statusText);
    //     // };
    //     xhr.send(JSON.stringify(data));
    // }

    function sendServerRequest(url, data) {
        console.log("Prepare to request");
        console.log(data);
        $.ajax({
            type: 'POST',
            url: url,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            dataType: 'json',
            //contentType: 'application/json; charset=utf-8',
            complete: function (result, status) {
                // Handle or verify the server response.
                window.location.reload();
                console.log("reloaded");
            },
            error: function(error){
                console.log(error);
            },
            data: data,
        });
    }

    function getCookie(name) {
        var value = "; " + document.cookie;
        var parts = value.split("; " + name + "=");
        if (parts.length === 2)
            return parts.pop().split(";").shift();
    }
}