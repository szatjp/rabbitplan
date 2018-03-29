/**
 * EasyUI DataGrid根据字段动态合并单元格
 * param tableID 要合并table的id
 * param colList 要合并的列,用逗号分隔(例如："name,department,office");
 * param mainColIndex 要合并的列索引集（针对要合并的列）
例如："0,1,2" 当然也可以是"0"也可以是"0,1"或者"1,2"这样
*/

function mergeCellsByField(tableID, colList, ColIndexArr) {
	var ColArray = colList.split(",");
	var indexArr = ColIndexArr.split(",");
	var tTable = $('#' + tableID);
	var TableRowCnts = tTable.datagrid("getRows").length;
	var tmpA;
	var tmpB;
	var PerTxt = "";
	var CurTxt = "";
	var alertStr = "";
	for ( var i = 0; i <= TableRowCnts; i++) {
		// 整理逻辑如果 几个关键列数据相等

		var tmp = ""
		if (i == TableRowCnts) {
			CurTxt = "";
		} else {
			for ( var kk = 0; kk < indexArr.length; kk++) {
				tmp += tTable.datagrid("getRows")[i][ColArray[indexArr[kk]]];
			}
			CurTxt = tmp
		}
		if (PerTxt == CurTxt) {
			tmpA += 1;
		} else {
			tmpB += tmpA;
			for ( var j = 0; j < ColArray.length; j++) {
				tTable.datagrid('mergeCells', {
					index : i - tmpA,
					field : ColArray[j],
					rowspan : tmpA,
					colspan : null
				});
			}
			tmpA = 1;
		}
		PerTxt = CurTxt;
	}
}

