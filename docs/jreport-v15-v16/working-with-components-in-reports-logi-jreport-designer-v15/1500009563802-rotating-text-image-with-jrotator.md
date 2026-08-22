---
title: "Rotating Text/Image with JRotator"
id: 1500009563802
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563802-Rotating-Text-Image-with-JRotator
updated_at: 2021-07-24T05:55:54Z
---

# Rotating Text/Image with JRotator

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584481-Creating-links-with-JHyperLink)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562902-Barcodes)

# Rotating Text/Image with JRotator

JRotator is used to rotate text or images. Since Logi JReport currently supports rotating only images but not text, using JRotator to achieve text rotation becomes a feasible solution. JRotator rotates the text inside the JRotator object but not the object itself so if you rotate text or DBFields you may have to change the size of the container in order to see the full value.

Below is a list of the sections covered in this topic:

> * [Using JRotator to Rotate Text](#Text)
> * [Using JRotator to Rotate an Image](#Image)
> * [Using JRotator to Rotate a DBField](#DBField)

## Using JRotator to Rotate Text

1. Start Logi JReport Designer and open the report in which you want to insert some rotated text.
2. Select **Insert** > **UDO** to display the Insert UDO dialog.
3. Select **JRotator** from the UDO drop-down list, and then select **OK**.
4. Keep the JRotator focused and go to the Report Inspector.
5. Locate the Display Value property and type in the required text in the value cell, then select outside of the cell. You will then see the typed text displayed in the JRotator.
6. Specify a rotation degree in the value cell of the Rotate property, for example, 180, then select outside of the cell. You will then find the text in the JRotator upside down.
7. Save the report.

## Using JRotator to Rotate an Image

1. Start Logi JReport Designer and open the report in which you want to insert a rotated image.
2. Select **Insert** > **UDO**.
3. In the Insert UDO dialog, select **JRotator** from the drop-down list, and then select **OK**.
4. Keep the JRotator focused and go to the Report Inspector.
5. Specify the local path of the required image in the value cell of the Display Image property, for example, *C:\image.jpg*, then select outside of the cell. You will then see the image displayed in the JRotator.
6. Specify a rotation degree in the value cell of the Rotate property, for example, 45, then select outside of the cell. You will then find the image in the JRotator at a 45 degree angle.
7. Resize the JRotator container as needed to view the entire image.
8. Save the report.

## Using JRotator to Rotate a DBField

1. Start Logi JReport Designer and open the report in which you want to insert a rotated DBField.
2. Select **Insert** > **UDO**.
3. In the Insert UDO dialog, select **JRotator** from the drop-down list, and then select **OK**.
4. Keep the JRotator focused and go to the Report Inspector.
5. In the Display Value value cell, select the required DBField or create a formula for a calculated field and select the formula from the dropdown list. Then select outside of the cell and you will see the DBField displayed in the JRotator.
6. Specify a rotation degree in the Rotate value cell, for example, 90, then select outside of the value cell. You will then find the DBField in the JRotator at a 90 degree angle.
7. Change the size of the JRotator container as needed to view the entire text.
8. Save the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584481-Creating-links-with-JHyperLink)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562902-Barcodes)
