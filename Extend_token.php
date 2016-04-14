<?php
//Extend token                                                                        

// Set Extended Access Token
$facebook->setExtendedAccessToken();

//Get access short live access token
$accessToken = $facebook->getAccessToken();

// Exchange token
$facebook->api('/oauth/access_token', 'POST',
array(  
    'grant_type' => 'fb_exchange_token',           
    'client_id' => 'APP ID',
    'client_secret' => 'APP Secret',
    'fb_exchange_token' => $accessToken
    )
    );

    // End extend access token
?>