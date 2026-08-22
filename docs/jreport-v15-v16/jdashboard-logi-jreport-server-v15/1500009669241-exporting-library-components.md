---
title: "Exporting Library Components"
id: 1500009669241
section: "JDashboard Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669241-Exporting-Library-Components
updated_at: 2021-07-24T20:55:18Z
---

# Exporting Library Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644822-Saving-Dashboards)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644762-Printing-Library-Components)

# Exporting Library Components

Library components visible in the page panel can be exported, for example, library components that were created using Logi JReport Designer and inserted into dashboards via the Resources panel.

To export the library components in a dashboard, select the **Export** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920358295/btn_expt.gif) on the toolbar, or select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar and select **Export** from the option list. Then in the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500009646042-Export#Dashboard) dialog, choose whether to use system layout or customize the layout. In the system layout, Logi JReport will calculate the positions of the library components in the dashboard following certain rule. If you are not satisfied with the system layout, you can customize the layout by yourself to determine the position of each library component and specify whether to export all the data of a table/crosstab or just the current page of the table/crosstab displayed in the dashboard. The customized layout can be saved for all users who can access the dashboard.

**To export using system layout:**

1. In the Export dialog, the **System Layout** item is selected as the layout by default.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920649879/expt_dshbd_sys.gif)

   The preview of the layout is displayed in the preview panel on the right. Sometimes you may find that the layout is a little different from what you see in the dashboard.
2. In the Resources box, select the library components you want to export. By default all exportable library components are listed and selected.
3. The order of the library components in the Resources box determines the order in which they will be exported. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif) and ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) to adjust the exporting order if necessary.
4. Check the **Show Component Title** option if you want to show the library component titles in the exported result.
5. Select the page navigation buttons on the toolbar of the preview panel to browse the pages if you want.
6. Select the **Page Setup** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920588183/btn_dshbrd_pgstup.gif) on the toolbar to set the page properties of the exported result file such as page size and margins in the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009670381-Page-Setup#Export) dialog. You can either define the page properties generally for all export formats or customize the page properties for each export format as you want.
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920358295/btn_expt.gif) to do the last setting and then export.
   1. From the Export File Format drop-down list, select the format to which the library components will be exported. For a format other than XML, all the selected library components will be exported into one single file. For XML, each library component will be exported to a separate XML file. When the exported result contains more than one file, all the files will be zipped.
   2. In the File Name text field, specify the name of the exported result file, which could be either a single file or a zipped package name.
   3. Check **Run Linked Report** if you need to include linked report in the exported result file.
   4. Select **OK** to start exporting.

**To customize the layout:**

1. In the Export dialog, select **Customize Layout** from the Layout drop-down list. You can also select an existing customized layout to modify it.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920593431/expt_dshbd.gif)
2. Check the **Show Component Title** option if you want to show the library component titles in the exported result.
3. Select the **Page Setup** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920588183/btn_dshbrd_pgstup.gif) on the toolbar to set the page properties of the exported result file such as page size and margins in the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009670381-Page-Setup#Export) dialog.
4. In the Design tab, customize the layout of the library components by making use of the following operations.
   The library components are arranged using a tabular with each cell holding one component.
   * Split or merge cells using the toolbar options: **![](https://devnet.logianalytics.com/hc/article_attachments/4404920586135/btn_dshbrd_splth.gif)**, **![](https://devnet.logianalytics.com/hc/article_attachments/4404920586391/btn_dshbrd_merge.gif)**, and **![](https://devnet.logianalytics.com/hc/article_attachments/4404926751511/btn_dshbrd_spltv.gif)**.
   * Drag a library component from the Resources box into a blank cell in the Design tab. A cell can hold only one library component.
   * Delete a library component from a tabular cell, by using the shortcut menu option Remove.
   * For a table or crosstab, only its current view of data as displayed in the dashboard will be exported by default. If you want its full data to be exported, right-click on the table or crosstab and select **Filter** from the drop-down list. Then in the Filter dialog, switch from Current View to **All** and select **OK**.
5. Select the **View** tab to preview the layout. You can browse the pages and zoom in/out by selecting the corresponding toolbar buttons.

   If you are satisfied with the layout and want to save it for future use, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926628119/btn_save.gif) or **![](https://devnet.logianalytics.com/hc/article_attachments/4404920358039/btn_saveas.gif)** on the toolbar, then in the Save As dialog, provide a name for the layout and select **OK**. The saved customized layouts will be available in the Layout drop-down list to all users who can access the dashboard. For each of them, you can edit its name or delete it using the two buttons - Rename and Delete - appearing on the right when the mouse hovers over the layout item on the drop-down list.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920585879/dshbrd_expt_layout.gif)
6. Select**![](https://devnet.logianalytics.com/hc/article_attachments/4404920358295/btn_expt.gif)**, then in the Export dialog, [do the last setting and start exporting](#Export).

**Tip:** If you just want to export a single library component, there is a more convenient way.

1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920355095/btn_dshbrd_more.gif) on the [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#TitleBar) and select **Export** from the drop-down menu. The Export dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920593175/expt_lc.gif)
2. In the dialog, choose the format to which you want to export the library component, then select **OK**.

However, using this way, if the library component is linked with other reports, you cannot control whether to generate the linked reports while exporting. The linked reports will not be included in the exported result.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644822-Saving-Dashboards)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644762-Printing-Library-Components)
