<?php
//連接資料庫
//只要此頁面上有用到連接MySQL就要include它
require_once __DIR__ . '/db_connect.php';
$db = new DB_CONNECT();
date_default_timezone_set('Asia/Taipei');

$serverName = "192.168.0.20"; //serverName
$connectionInfo = array( "Database"=>"stipendiary", "UID"=>"sa", "PWD"=>"csii1qaz@WSX","CharacterSet"=>"UTF-8");
$conn = sqlsrv_connect( $serverName, $connectionInfo);

$area = @$_POST['area'];
$objectID = $_POST['objectID'];
$objectName = $_POST['objectName'];
$objectValue = $_POST['objectValue'];
$datetime = date ("Y-m-d");

if($objectID == 2001){
	$area = 301;
}

if($area  !=  ""  &&  $objectID  !=  ""  &&  $objectName  !=  ""  &&  $objectValue  !=  ""){
	//echo $area;
	$mySQLInsert = "INSERT INTO `".$area."` (area,objectID,objectName,objectValue,date) VALUES ('$area','$objectID','$objectName','$objectValue','$datetime')"; //插入資料到資料庫裡
	$mySQLQuery_state = mysql_query($mySQLInsert);
	//Mssql
	$msSQLInsert = "INSERT INTO [dbo].[".$area."] (area,objectID,objectName,objectValue) VALUES ('$area','$objectID','$objectName','$objectValue')";
	$msSQLQuery_state = sqlsrv_query($conn,$msSQLInsert);
	if($msSQLQuery_state && $mySQLQuery_state){
		echo "insert success";
	}else{
		die('msSQL Invalid query: '.print(sqlsrv_errors()));
		die('mySQL Invalid query: '.print(mysql_error()));
	}
}
else{
	echo "your data aren't complete";
}



?>
