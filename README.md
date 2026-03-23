note : recreate repo and add this files becase i added some unwanted comments that i create at time of scrpit development..

1] captch_image.jpg -> auto downloaded by automation scrpit (drissionpage)
2] drissionpage_automation -> this scrpit has main logic 
--> i create temp profile that work as incognito profile , that help to create profile that has no cookies.
--> then hit request on page 
--> get image save it , 
--> read that image with paddleOCR -> use_textline_orientation -- i want to read text from image so make this "True"
-->take captch value in "detected_text"
--> enter that value in input box and click on "Check" button 
--> Done..

3] output_result
--> i take SS of output that done by drissionpage and paddleocr scrpit and attaching it in this folder.


-------------------------------
