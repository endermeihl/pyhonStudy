<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>td加斜线</title>
<style>
table{
border-collapse:collapse;
}
table,tr,td{
border:1px solid black;
}
td{
width:100px;/*这里需要自己调整，根据自己的需求调整宽度*/
height:50px;/*这里需要自己调整，根据自己的需求调整高度*/
position: relative;
}
td[class=first]:before{
content: "";
position: absolute;
width: 1px;
height:114px;/*这里需要自己调整，根据td的宽度和高度*/
top:0;
left:0;
background-color: white;
display: block;
transform: rotate(-63deg);/*这里需要自己调整，根据线的位置*/
transform-origin: top;
}

</style>
</head>
<body>
<table>
<tr>
<th>姓名</th>
<th>年龄</th>
<th>性别</th>
</tr>
<tr>
<td class="first">11</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</table>
</body>