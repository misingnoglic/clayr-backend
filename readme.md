If you've ever gotten a lab test from your doctor, you know they can look a big confusing and disorienting. People want to know what's wrong with them, not all these confusing statistics: ![Imgur](http://i.imgur.com/m9Kfe87.jpg)

Now compare that to this:
![Imgur](http://i.imgur.com/aeqBoyM.jpg)

What our app does is allow a user or doctor to take a picture of their lab results and see clearly what the results mean. People who are more involved in their health consistently are healthier than those who do not, so we want to enable everyone to have a low barrier access to their data. 

The app works by sending images of the lab tests to our Django server (hosted by Microsoft Azure), which then processes the pictures into text and then generates JSON data after doing tests. The app then uses that JSON to synthesize the readable tests and let the user see what's going on. Behind the scenes it's a fairly complicated process, but for the user it's seamless and integrates quickly and easily.

Here's an image of the original picture, next to the OCR, next to the JSON, it's fairly amazing how accurate this got.
![Imgur](http://i.imgur.com/MKZipj8.png) 

This was a project that was a reach project for everyone on the team, and given more time there's a few more features we would want. For example, a lot of hospitals and doctors are moving to digital formats such as Blue button, and we would want a way to integrate that data into the app. We would also want a way to consolidate the different environments into one single interface (on web, android, and iOS). There are also a lot of security concerns to be dealt with, and monetization issues (as we're running on lots of free trial software). Most of the design images are mockups, but it's all feasible and the technology is working. It's just a matter of implementation at this point, but we're hoping by demo it will be as close to this as possible.

It was an ambitious idea, but we hope it's one you can feel hopeful about. People who are more involved in their health are bound to live more healthy lives, and we're hoping this app helps stimulate this involvement with a low barrier entry into understanding your own body and self.

Credits: 

Chen: Design, Hosting, Android App, OCR, medical liaison, being a superhero in general 

Arya: Django/Python backend, OCR/ABBYY, Challengepost

Stefan: Android App

Josh: iOS