---
title: "Working with Images"
id: 45190450620813
section: "Working with Components in Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190450620813-Working-with-Images
updated_at: 2026-04-30T15:12:18Z
source_host: logi-report-v26.insightsoftware.com
---
# Working with Images

An image is a digital representation of a picture. Report supports the following image formats: .bmp, .gif, .jpg, and .png. This topic describes how you can insert images into a report.

For the images in a report, you can use them as the trigger object of links.

To insert an image in a report

- Position the mouse pointer at the allowed report location where you want to insert the image.
				

- Do one of the following:
			    
- From the Components panel, drag the Image icon  in the Basic category. 

- Navigate to Insert > Image.

- Navigate to Home > Insert > Image.

Designer displays the Select an Image dialog box.

- Select the image you want to use. 
- If you want to use an image from your local file system, use the Look in drop-down list to browse for the image, then select Open. If the image file is not in the current catalog directory, Designer prompts you  to copy it to the directory.

- If you want to use an image via URL, type the URL in the URL text box and select OK. When you save the report, Designer saves the URL information into the report template. If you are in an intranet, to successfully access an image via URL, you need to add the -DproxyHost and -DproxyPort options to the CLASSPATH environment variable of Designer's startup file JReport.bat in <install_root>\bin to specify the intranet information.

See an example: The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the image component example, open <install_root>\Demo\Reports\SampleComponents\ForImage.cls.
