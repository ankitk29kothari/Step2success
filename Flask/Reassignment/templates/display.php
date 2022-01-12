<html>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
		<script src="jquery.dataTables.min.js"></script>
		<script src="https://cdn.datatables.net/1.10.12/js/dataTables.bootstrap.min.js"></script>	
		<link rel="stylesheet" href="https://cdn.datatables.net/1.10.12/css/dataTables.bootstrap.min.css" />
		
		
		
		<script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>

		
		
		<script src="../lib/jquery.min.js"></script>
<script src="dist/jquery.handsontable.full.js"></script>
<link rel="stylesheet" media="screen" href="dist/jquery.handsontable.full.css">
</head>

<body>
    <table id="example" class="display" cellspacing="0" width="100%">
        <thead>
            <tr>
                <th>Cascade</th>
                
        </thead>
		         <form class="form-inline signup" role="form"  method = post action =''>
        <tbody>
            <tr>
                <td><input  type="text"name="a[1]" ></td>
				</tr>
            <tr>
                <td><input type="text" name ="a[2]"></td>
				</tr>
            <tr>
                <td><input  type="text" name ="a[3]"></td>
            </tr>
            <tr>
                <td><input type="text" name="a[4]"></td>
				</tr>
            <tr>
                <td><input type="text" name="a[5]"></td>
				</tr>
            <tr>
                <td><input type="text" name="a[6]"></td>
            </tr>
            <tr>
                <td><input type="text" name="a[7]"></td>
				</tr>
            <tr>
                <td><input type="text" name="a[8]"></td>
				</tr>
            <tr>
                <td><input type="text" name="a[9]"></td>
            </tr>
			   <tr>
                <td><input type="text" name="a[10]"></td>
            </tr>
        </tbody>
		<input type='submit' name ='submit' value ='submit'  class="btn btn-theme"></button>
    </table>

    <script>
        $(document).ready(function () {
            $('td input').bind('paste', null, function (e) {
                $txt = $(this);
                setTimeout(function () {
                    var values = $txt.val().split(/\s+/);
                    var currentRowIndex = $txt.parent().parent().index();
                    var currentColIndex = $txt.parent().index(); 
                    
                    var totalRows = $('#example tbody tr').length;
                    var totalCols = $('#example thead th').length;
                    var count =0;
                    for (var i = currentColIndex; i < totalCols; i++) {
                        if (i != currentColIndex)
                            if (i != currentColIndex)
                                currentRowIndex = 0;
                        for (var j = currentRowIndex; j < totalRows; j++) {                           
                            var value = values[count];
                            var inp = $('#example tbody tr').eq(j).find('td').eq(i).find('input');
                            inp.val(value);
                            count++;
                           
                        }
                    }


                }, 0);
            });
        });
    </script>



<?php

include 'fetch.php';
/*include database configuration file
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "bp";
 
// Create connection
 
$conn = mysqli_connect($servername, $username, $password, $dbname);

//get records from database



if(isset($_POST['submit']))
{
	
	extract($_POST);//creates variables from array
//print_r($_POST);

	


?>	
<div id="dataTable">
<table    cellspacing="0" width="50%">


        <thead>
            <tr>
                <th>UNI Pon</th>
				<th>UNI sent Date</th>
                <th>UNI sup date</th>
                <th>UNi Foc Date</th>
                <th>EVC1 Pon</th>
                <th>EVC2 Pon</th>
				<th>EVC1 sent Date</th>
				<th>EVC1 sup Date</th>
				<th>EVC1 Foc Date</th>
            </tr>
        </thead>

		<tbody>	
		
		 			<?php 

/*
for ($i = 1; $i <= 10; $i++){
 $sql = ("SELECT * FROM augment WHERE cascades= '$a[$i]'");



$result=mysqli_query($conn,$sql);


if (mysqli_num_rows($result)> 0) {

			    while($row = mysqli_fetch_assoc($result)) {
					
					if ($row["evc1_sup_date"]=="0000-00-00"){
$row["evc1_sup_date"]="";	
	
}

if ($row["uni_date"]=="0000-00-00"){
$row["uni_date"]="";	
	
}

if ($row["uni_sup_date"]=="0000-00-00"){
$row["uni_sup_date"]="";	
	
}

if ($row["uni_foc"]=="0000-00-00"){
$row["uni_foc"]="";	
	
}
	
	
		 


			echo "<tr>
					<td>".$row["uni_pon"]."</td>
					<td>".$row["uni_date"]."</td>
					<td>".$row["uni_sup_date"]."</td>
					<td>".$row["uni_foc"]."</td>
					<td>".$row["evc1_pon"]."</td>
					<td>".$row["evc2_pon"]."</td>
						<td>".$row["evc1_date"]."</td>
							<td>".$row["evc1_sup_date"]."</td>
								<td>".$row["evc1_foc"]."</td>
					
				
					</tr>";
				}					
 }}
}
			
	*/
	?>
  </tbody>
  </div>	
    </table>	
