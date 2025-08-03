# pythoncaptchasystem
a FREE Python captcha system coded entirely in python, it generates a html on the spot and all you need to do is input your site key AND secret key from hcaptcha
it runs on  a service called "hCaptcha", which is a free alternative to reCaptcha V2/V3,which is owned by google and the free plans there are limited
The reason i chose hcaptcha over cloudfare, or Friendly Captcha, was that hcaptcha allowed me to secure it better as it generates a brand new .html everytime, and that file only runs when the python script tells it to.


To work the file, first download the CUSTOMCAPTCHA.py file from this repo, then open a new account on hcaptcha on their free plan. Copy and paste the scret key they give into a notepad doc, if you dont get it go to settings and click reset secret key.
Click on the "Sites" tab, and click add a new site, name it whatever you want and under the "Domains", add 127.0.0.1. That will ensure it runs locally, while the data is still being sent to hcaptcha's servers.
Then you can choose what you want under "hcaptcha behaviour" and the "Passing Threshold" sections.
Then click save, and click the site again, and now you should see a new section, called "Sitekey", copy it and paste it into the same notepad document you pasted the secret key into.
Then open the CUSTOMCAPTCHA.py file on your preffered IDE(eg, stock , vs code, etc),  Then Open the notepad document you saved your keys into, and paste them into the part of the code where it says "YOUR_SITE_KEY" and "YOUR_SECRET_KEY" , do NOT share them.
Thats pretty much it, all you need to do now is to paste your desired code at the end of the file.
Your Done!!!!
