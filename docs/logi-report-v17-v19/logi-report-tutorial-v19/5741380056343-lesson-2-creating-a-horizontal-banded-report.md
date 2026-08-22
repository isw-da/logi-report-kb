---
title: "Lesson 2: Creating a Horizontal Banded Report"
id: 5741380056343
section: "Logi Report Tutorial v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741380056343-Lesson-2-Creating-a-Horizontal-Banded-Report
updated_at: 2024-02-05T19:06:23Z
---

# Lesson 2: Creating a Horizontal Banded Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741398712727-Lesson-1-Creating-a-Standard-Banded-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741384902295-Lesson-3-Creating-a-Mailing-Label-Report)

# Lesson 2: Creating a Horizontal Banded Report

Your new reporting assignment is to create a summary of each Jinfonet Gourmet Java employee. The report also needs to communicate the ranking of the employee's salary, that is, whether it is on the upper or lower end, or somewhere in between, relative to all employees.

The following prototype of the report has been given to you:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/9905877858071/rpt_lsn2_model.gif)

Follow these tasks to create the report:

* [Task 1: Create the Initial Report](#Task1)
* [Task 2: Adjust the Report Layout and Add the Photo DBField](#Task2)
* [Task 3: Rank the Employees](#Task3)
* [Task 4: Fine Tune the Report Layout](#Task4)

## Task 1: Create the Initial Report

Again, the report has repeated rows of information, but this time they are repeated left to right instead of top down. Logi Report offers the horizontal banded layout to support this format.

To create the initial report with a horizontal banded object, follow these steps:

1. In Designer, navigate to **File** > **New** > **Page Report**.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) Be sure that JinfonetGourmetJava.cat is the current catalog because this is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Steps 3 and 4](https://devnet.logianalytics.com/hc/en-us/articles/5741398712727-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
2. In the Select Component for Page Report dialog box, select **Horizontal Banded**, then select **OK**.
3. In the **Data** screen of the Horizontal Banded Wizard dialog box, select **<New Query...>** in the Queries node of Data Source 1, type **EmployeeInformation** in the Enter Query Name dialog box and select **OK**.
4. In the Add Tables/Views/Queries dialog box, expand the JDBC connection node and then the **Tables** node, then select the table **Account Managers** and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905875055127/btn_addarw.gif) to add it to the query. Select **OK** to close the dialog box.
5. In the Query Editor dialog box, select **\*** in the **Account Managers** table to add all the columns in it to the query and then select **OK** to create the query.
6. Select **Next** in the Horizontal Banded Wizard dialog box to go to the next screen.
7. In the **Display** screen, drag the following DBFields from the **Resources** box to the right box one by one: **Name**, **Employee Position**, **Notes**, **HireDate**, **Birthday**, and **Home Phone**, then edit the display names of HireDate and Birthday to **Hire Date** and **Birth Date**. Select **Next**.

   ![Add Display Fields](https://devnet.logianalytics.com/hc/article_attachments/9905899876375/rpt_lsn2_dsply.gif)
8. In the **Group** screen, select **Account Manager ID** and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905875055127/btn_addarw.gif) to add it as the group-by field.
9. Select **Style** on the screen navigation bar to switch to the screen and select **Simple** as the report style.
10. Select **Finish** to create the report.

    Designer identifies the panels in the banded object on the top by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a group header panel (GH), a detail panel (DT), a group footer panel (GF), a banded page footer panel (BPF), and a banded footer panel (BF).

    ![Banded Panels](https://devnet.logianalytics.com/hc/article_attachments/9905899912215/rpt_lsn2_intlrpt.gif)

## Task 2: Adjust the Report Layout and Add the Photo DBField

In this task, we want to adjust the layout of the report first to improve the appearance of the report. Then, we need to add the Photo field to the report which enables users of the report to identify the employee.

1. Widen the DT panel, then resize the **Employee Position** and **Notes** DBFields horizontally so that the data does not get truncated.

   ![Resize DBFields](https://devnet.logianalytics.com/hc/article_attachments/9905899933207/rpt_lsn2_wdn.gif)
2. Select the **Name**, **Employee Position**, and **Notes** labels in the BPH panel, then select **Delete** on the keyboard to remove them from the report.

   ![Delete Labels](https://devnet.logianalytics.com/hc/article_attachments/9905899948567/rpt_lsn2_dltlbl.gif)
3. Adjust the space between fields in the DT panel, move the **Hire Date**, **Birth Date**, and **Home Phone** name labels from the BPH panel to the DT panel and place them above their fields.

   ![Move Labels](https://devnet.logianalytics.com/hc/article_attachments/9905877972375/rpt_lsn2_spc.gif)
4. Hide the BH, BPH, GF, BPF, and BF panels that do not hold any data by right-clicking the panel and selecting **Hide** from the shortcut menu.
5. Resize the GH panel, navigate to **Insert** > **Label** to add a label before the group-by field in the panel, double-click the label to edit its text as "**Employee ID:**", then resize the group-by field and the label and adjust their position as follows:

   ![Add Label](https://devnet.logianalytics.com/hc/article_attachments/9905899998743/rpt_lsn2_id.gif)
6. From the **Data** panel, drag the **Photo** DBField to the GH panel.
7. Remove the name label of the Photo DBField by right-clicking it and selecting **Delete** from the shortcut menu, then resize the field as follows:

   ![Add Photo](https://devnet.logianalytics.com/hc/article_attachments/9905900037399/rpt_lsn2_photo.gif)
8. Navigate to **Insert** > **Drawing Object** > **Line** to insert a Line object below the first field in the DT panel, and insert a box object in the same way to enclose all the objects in the reports.

   ![Insert Drawing Objects](https://devnet.logianalytics.com/hc/article_attachments/9905900070807/rpt_lsn2_box.gif)

## Task 3: Rank the Employees

As required at the beginning of the report design, the manager wants to rank the employees by their salaries, so we need to add a rank object to the report.

1. Select the DT panel of the report and navigate to **Insert** > **Rank**.
2. In the Rank Expert dialog box, select **Salary** from the **Rank Resources** box.
3. Select **Browse**, choose **Rank5.gif** in the **JinfonetGourmetJava** folder and select **Open** to select it as the default image for all value ranges.
4. In the **Value Range** box, type **40000** in the **Minimum** column and **49999** in **Maximum**, then select in the **Image** column and select **<Browse...>** to choose **Rank3.gif** as the image of this range.
5. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905874723735/btn_add.gif) twice to add two ranges and define them as follows:

   ![Define Ranks](https://devnet.logianalytics.com/hc/article_attachments/9905900105239/rpt_lsn2_addrnk.gif)
6. Select **Insert** to insert the rank to the DT panel, below the **Home Phone** field.
7. Move the name label **Salary** of the rank from the bottom of GH panel and place it above the rank, then edit its text to **Salary Ranking** and resize the label to full display the text.

   ![Insert Ranks](https://devnet.logianalytics.com/hc/article_attachments/9905878092055/rpt_lsn2_rank.gif)

## Task 4: Fine Tune the Report Layout

1. Select the **Employee ID** label and the group-by field in the GH panel, then select **10** from **Font Size** drop-down list ![Font Size button](https://devnet.logianalytics.com/hc/article_attachments/9905899755543/btn_fontsz.gif) in the **Format** ribbon.
2. Select the **Salary Ranking** label and the rank in the DT panel, then navigate to **Format** > **Left**![Left Align button](https://devnet.logianalytics.com/hc/article_attachments/9905878121751/btn_alignleft.gif) to align them the same with other objects in the DT panel.
3. Select the first field in the DT panel (the Name DBField), change its properties in the Report Inspector as follows, then resize it to make sure the names can display completely.
   * Font Size: 12
   * Bold: true
   * Foreground: 0xcc0000
4. Right-click the **Photo** DBField in the GH panel and select **Display Type** from the shortcut menu.
5. In the Display Type dialog box, select **Image** in the **Display As** box, choose **GIF or JPG** from the **Decode Type** drop-down list, then select **OK**.

   ![Display Field as Image](https://devnet.logianalytics.com/hc/article_attachments/9905900261527/rpt_lsn2_img.gif)
6. In the Report Inspector, select the **Line** node in the report structure tree and change its **Line Color** property to **Lightgray** and **Line Thickness** to **0.02**.

   ![Edit Line Properties](https://devnet.logianalytics.com/hc/article_attachments/9905900300439/rpt_lsn2_lnprpty.gif)
7. Select the **Box** node and change its **Border Color** property to **Lightgray** too.

Next, we want to add a title to the report to the page header panel of the report.

1. Select **Page Header** in the **View** ribbon to display the page header.
2. In the Report Inspector, select the **Page Header Panel** node and change its **Height** property to **0.6**.
3. From the **Components** panel, drag the **Label** icon ![Label button](https://devnet.logianalytics.com/hc/article_attachments/9905897864599/btn_label.gif) to the page header panel to add a label in it.
4. Resize the label, double-click it to modify its text as **Employee Information List**, then in the Report Inspector, change its **Font Size** to **14**, and **Foreground** to **0xcc0000**.

   After editing, the report looks somewhat as follows in design view:

   ![Report in Design View](https://devnet.logianalytics.com/hc/article_attachments/9905878200727/rpt_lsn2_dsgn.gif)
5. On the report tab bar, right-click the report tab and select **Rename** to rename it to **EmployeeDetails**.

   ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/9905863488151/renmrpttb.gif)
6. Navigate to **File** > **Save** to save the report as **EmployeeInformation.cls**.
7. Select the **View** tab to preview the report. Designer displays the report similar to this:

   ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/9905900360471/rpt_lsn2_prvw.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\TutorialReports`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741398712727-Lesson-1-Creating-a-Standard-Banded-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741384902295-Lesson-3-Creating-a-Mailing-Label-Report)
