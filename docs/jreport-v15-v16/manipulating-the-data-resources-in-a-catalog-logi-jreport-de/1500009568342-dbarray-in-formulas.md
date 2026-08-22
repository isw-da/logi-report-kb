---
title: "DBArray in Formulas"
id: 1500009568342
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568342-DBArray-in-Formulas
updated_at: 2021-07-24T05:54:35Z
---

# DBArray in Formulas

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589721-User-Defined-Formula-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties)

# DBArray in Formulas

Logi JReport Designer supports a multiple-value field, which contains a set of values in a single field, in a formula. Using the multiple value field is the same as using an array in a formula. You can refer to a field with multiple values as with a normal field in a formula, such as @FIELDNAME, and then use the array functions that Logi JReport Designer provides in the Formula Eitor to manipulate the values in it. Logi JReport Designer first converts this field into a normal array, and then manipulates it in the usual way.

For example, normally an array in a formula is manually defined as follows:

`Integer myArray[4]=[1, 2, 3, 4]; //Datatype ArrayName[ArraySize]=[ArrayContent];`

The array may be referred to in this way:

`integer myInt=3;  
myInt in myArray;`

If a field, named myField, for example, contains a similar array value, it can be referred to similarly:

`integer myInt=3;  
myInt in @myField;`

If you want to display all the values of an array use the [join()](https://devnet.logianalytics.com/hc/en-us/articles/1500009568262-String-Functions#join) function to return a string of all the values.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589721-User-Defined-Formula-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties)
