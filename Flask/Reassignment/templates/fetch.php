


<?php




include('db.php');
include('function.php');
$query = '';
$output = array();
$data = array();
session_start();
$p= $_SESSION['name'] ;
//echo "name";
//echo $_SESSION['name'];
//echo $p;
if(isset($_POST['data']))
{	
$_SESSION['data']  = $_POST['data'];	


//print_r($_SESSION['data']);


foreach ($_POST['data'] as $value) {
    $c= trim($value[0]);
     $c1= trim($value[1]);




$query = '';
		
 $query = "UPDATE augment SET provisoner='$c1' WHERE cascades ='$c' ORDER BY  ass_date DESC LIMIT 1";


	if ($c1!=""){
$statement = $connection->prepare($query);
$statement->execute();
//$result = $statement->fetchAll();
}


	$sub_array = array();
	$sub_array[] = $c;
	$sub_array[] = $c1;

	if ($c1!=""){

		$sub_array[] = "Reassigned";
	}
	
	
	

	$data[] = $sub_array;



//print_r( $data);
//echo '<br>';
}

$_SESSION['out'] = array(
	
	"data"				=>	$data
);

}
echo json_encode($_SESSION['out']);



?>