If you enter your name and sub‐
mit it, and then click the refresh button in your browser, you will likely get an
obscure warning that asks for confirmation before submitting the form again. This
happens because browsers repeat the last request they sent when they are asked to
refresh a page. When the last request sent is a POST request with form data, a refresh
would cause a duplicate form submission, which in almost all cases is not the desired
action. For that reason, the browser asks for confirmation from the user.


Many users do not understand this warning from the browser. Consequently, it is
considered good practice for web applications to never leave a POST request as the last
request sent by the browser.


This is achieved by responding to POST requests with a redirect instead of a normal
response. A redirect is a special type of response that contains a URL instead of a
string with HTML code. When the browser receives a redirect response, it issues a 
GET request for the redirect URL, and that is the page that it displays. The page may
take a few more milliseconds to load because of the second request that has to be sent
to the server, but other than that, the user will not see any difference. Now the last
request is a GET , so the refresh command works as expected. This trick is known as
the Post/Redirect/Get pattern.


But this approach brings a second problem. When the application handles the POST
request, it has access to the name entered by the user in form.name.data , but as soon
as that request ends the form data is lost. Because the POST request is handled with a
redirect, the application needs to store the name so that the redirected request can
have it and use it to build the actual response.


Applications can “remember” things from one request to the next by storing them in
the user session, a private storage that is available to each connected client.

