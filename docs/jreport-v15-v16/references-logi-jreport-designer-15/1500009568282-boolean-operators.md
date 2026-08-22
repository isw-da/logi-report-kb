---
title: "Boolean Operators"
id: 1500009568282
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568282-Boolean-Operators
updated_at: 2021-07-24T05:54:38Z
---

# Boolean Operators

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589601-Comparison-Operators)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589621-Other-Operators)

# Boolean Operators

Below is a list of the Boolean operators used in Logi JReport Designer:

> * [x || y](#1)
> * [x && y](#2)
> * [!x](#3)

Below is a set of truth tables showing the logic operations for 3-valued logic.

| A AND B | True | False | Null |
| --- | --- | --- | --- |
| True | True | False | Null |
| False | False | False | False |
| Null | Null | False | Null |

| *A* OR *B* | True | False | Null |
| --- | --- | --- | --- |
| True | True | True | True |
| False | True | False | Null |
| Null | True | Null | Null |

| *A* | NOT *A* |
| --- | --- |
| True | False |
| False | True |
| Null | Null |

## Boolean x || Boolean y

Returns true if x is true or y is true.

**Examples**

* The return value of the following statement is abc.

  `Integer s=4,d=8;  
   Integer f=6;  
   if ( f>s || f>d )  
   {  
   return "abc";  
   }`
* `if ((@"Annual Sales" > 50000) ||(@"Annual Sales"<0)) then   
   "Customer needs attention"   
   else   
   "Normal customer"`
* `If( ! isNull(@customerId) && ! isNull(@country)){  
                  If(@customerId > 10 || @country == ‘USA’){  
                                 Integer newId =  @customerId + 1;  
   }  
   }  
   Else{  
                  // Some error processing logic here`  
   }

## Boolean x && Boolean y

Returns true if x is true and y is true.

**Examples**

* The return value of the following statement is abc.

  `Integer s=4,d=8;  
  Integer f=6;  
  if ( f>s && f<d )  
  {  
  return "abc";  
  }`
* `if ((@"Annual Sales" <3000) && (@Customers_Country=="USA")) then   
  "Customer is in the USA and Annual Sales is less than 3000"   
  else   
  "Others"`

## ! Boolean x

Returns true if x is false.

**Example**

The return value of the following statement is def.

`Integer s=4, d=8;  
Integer f=6;  
if ( ! ( f>s ) )  
return  "abc"  
else  
return "def"`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589601-Comparison-Operators)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589621-Other-Operators)
