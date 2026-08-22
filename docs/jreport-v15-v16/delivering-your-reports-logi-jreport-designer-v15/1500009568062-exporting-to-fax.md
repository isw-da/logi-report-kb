---
title: "Exporting to Fax"
id: 1500009568062
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568062-Exporting-to-Fax
updated_at: 2021-07-24T05:54:40Z
---

# Exporting to Fax

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589401-Exporting-to-PostScript)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589241-Exporting-to-Applet)

# Exporting to Fax

Logi JReport Designer provides the feature of exporting the report results to fax either via a fax machine or a fax server. If you require this feature to be enabled, you will first need to configure your running environment.

Download the files listed in the tables below from our website (<http://www.jinfonet.com/download/third_party_tool/JavaCommAPIV2_Win32.zip> or [http://www.jinfonet.com/download/third\_party\_ tool/JavaCommAPIV2\_Solaris.zip](http://www.jinfonet.com/download/third_party_tool/JavaCommAPIV2_Solaris.zip)), and put them in the specified locations:

* For Windows

  | File Name | Location |
  | --- | --- |
  | comm.jar | `<Java_install_root>\jre\lib\ext` |
  | javax.comm.properties | `<Java_install_root>\jre\lib` |
  | Win32Com.dll | `<Java_install_root>\jre\bin` |

* For Solaris

  | File Name | Location |
  | --- | --- |
  | comm.jar | `<Java_install_root>/jre/lib/ext` |
  | javax.comm.properties | `<Java_install_root>/jre/lib` |
  | libSolarisSerialParallel.so | `LD_LIBRARY_PATH` |

Meanwhile, before you can export report results to fax, you need to have settings of the fax machine or fax server configured. Otherwise a warning message will be displayed when you try to export to fax. To do this:

1. Select **File** > **Options**.
2. In the Options dialog, select the **Export to** category.
3. In the Fax tab, specify via which you want to fax the report results: fax machine or fax server.
4. Configure settings of the fax machine/server as required (For details about the settings, refer to [Export to - Fax](https://devnet.logianalytics.com/hc/en-us/articles/1500009588081-Options-Dialog#Fax)).
5. Select **OK** to accept the changes.

Now, you can export your report results to fax as follows:

1. Open the report you want to export.
2. Select **File** > **Export**  > **To Fax**.
3. In the [Export to Fax](https://devnet.logianalytics.com/hc/en-us/articles/1500009586701-Export-to-Fax-Dialog) dialog, specify the settings as required.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893842583/expt2fax.gif)
4. When done, select **OK** to generate the file.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589401-Exporting-to-PostScript)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589241-Exporting-to-Applet)
