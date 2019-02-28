<?php
    require 'sconfig.php';

    $mysqli = mysqli_connect($host, $user, $password, $database);

    require 'query_function.php';

    $sql = "SELECT id,name,COUNT(id) as clubs
            FROM players
            GROUP BY id
            ORDER BY clubs DESC";

    $response = runQuery($mysqli,$sql);
    
    //preformat our text
    echo "<pre>";

    if($response['success']) {
        $data = $response['result'];

        echo "1.) Teams played for: \n\n";
        echo "# \t ID \t\t Name\t\tTeams\n";
        echo "======================================\n";
        for($i = 0; $i < 10; $i++)
        {
            echo "$i \t {$data[$i]['id']} \t {$data[$i]['name']} \t {$data[$i]['clubs']}\n";
        }
    }
    else{
        echo $response['error'];
    }

    //=================================================================================================
    $sql = "SELECT `playerid`,`season`,SUM(yards) AS total_yards\n"
        ."FROM `players_stats`\n"
        . "WHERE `statid` = 10\n"
        . "GROUP BY `playerid`,`season`\n"
        . "ORDER BY total_yards DESC";

    $response = runQuery($mysqli,$sql);

    if($response['success']){
        $data = $response['result'];
        echo "\n2.) Rushing Yards: \n\n";
        echo "# \t ID \t\t Name\t\tYear\t Yardage\n";
        echo "==================================================\n";
        //I'll try to remember to add name to this field
        for($i = 0; $i < 5; $i++)
        {
            $pname = nameByID($mysqli,$data[$i]['playerid']);
            echo "$i \t {$data[$i]['playerid']} \t $pname  \t {$data[$i]['season']} \t {$data[$i]['total_yards']}\n";
        }

    }
    else{
        echo $response['error'];
    }
            
    //=============================================================================================================

    $sql = "SELECT `playerid`,`season`,SUM(yards) AS total_yards\n"
        .   "FROM `players_stats`\n"
        .   "WHERE `statid` = 15\n"
        .   "GROUP BY `playerid`\n"
        .   "ORDER BY total_yards";

    $response = runQuery($mysqli,$sql);

    if($response['success']){
        $data = $response['result'];
        echo "\n3.) Top 5 Worst Passers: \n\n";
        echo "# \t ID \t\t Name\t\tYear\t Yardage\n";
        echo "==================================================\n";
        for($i = 0; $i < 5; $i++)
        {
            $pname = nameByID($mysqli,$data[$i]['playerid']);
            echo "$i \t {$data[$i]['playerid']} \t $pname \t {$data[$i]['season']} \t {$data[$i]['total_yards']}\n";
        }
    
    }
    else{
        echo $response['error'];
    }
    ////////////////////////////////////////////////////////////////////////////////////////////////////////
    $sql = "SELECT `playerid`,COUNT(yards) AS total_yards\n"
        .   "FROM `players_stats`\n"
        .   "WHERE `statid` = 10 AND `yards` < 1\n"
        .   "GROUP BY `playerid`\n"
        .   "ORDER BY total_yards DESC";

    $response = runQuery($mysqli,$sql);

    if($response['success']){
        $data = $response['result'];
        echo "\n4.) Top 5 Worst Rushers: \n\n";
        echo "# \t ID \t\t Name\t\t Lossy Rushes\n";
        echo "==================================================\n";
        //I'll try to remember to add name to this field
        for($i = 0; $i < 5; $i++)
        {
            $pname = nameByID($mysqli,$data[$i]['playerid']);
            echo "$i \t {$data[$i]['playerid']} \t $pname  \t {$data[$i]['total_yards']}\n";
        }
    
    }
    else{
        echo $response['error'];
    }
    /////////////////////////////////////////////////////////////////////////////////////////////////

    $sql = "SELECT `club`,COUNT(`statid`) AS penalties\n"
        .   "FROM `players_stats`\n"
        .   "WHERE `statid` = 93\n"
        .   "GROUP BY `club`\n"
        .   "ORDER BY penalties DESC";

    $response = runQuery($mysqli,$sql);

    if($response['success']){
        $data = $response['result'];
        echo "\n5.) Top 5 teams with the most penalties: \n\n";
        echo "# \t Team \t\t penalties\n";
        echo "==================================================\n";

        for($i = 0; $i < 5; $i++)
        {
            echo "$i \t {$data[$i]['club']} \t\t {$data[$i]['penalties']}\n";
        }
    
    }
    else{
        echo $response['error'];
    }
////////////////////////////////////////////////////////////////////////////////////////////

    $sql = "SELECT `season`,COUNT(`statid`) AS penalties,COUNT(DISTINCT(`gameid`)) AS total_games\n"
        .   "FROM `players_stats`\n"
        .   "WHERE `statid` = 93\n"
        .   "GROUP BY `season";

    $response = runQuery($mysqli,$sql);

    if($response['success']){
        echo "\n6.) Average Penalties/Season: \n\n";
        echo "# \t Season \t total penalties \t average\n";
        echo "==================================================\n";
        $data = $response['result'];

        for($i=0; $i < 10; $i++){
            $avg = $data[$i]['penalties'] / $data[$i]['total_games'];
            echo "$i \t {$data[$i]['season']} \t\t {$data[$i]['penalties']} \t\t $avg \n";
        }

    }
    else{
        echo $response['error'];
    }

///////////////////////////////////////////////////////////////////////////////////////////////////////////
//              SPACE RESERVED FOR 7th(Q6)  SOLUTION
//              team with lowest avg plays each season
///////////////////////////////////////////////////////////////////////////////////////////////////////////


    $sql = "SELECT `playerid`,COUNT(`statid`) AS goal_kicks\n"
        .   "FROM `players_stats`\n"
        .   "WHERE `statid` = 70 AND `yards` > 40\n"
        .   "GROUP BY `playerid`\n"
        .   "ORDER BY goal_kicks DESC";

    $response = runQuery($mysqli,$sql);
    
    if($response['success']){
        echo "\n8.) Most goal kicks over 40 yards: \n\n";
        echo "# \t id \t\t Name \t\t Kicks\n";
        echo "==================================================\n";
        $data = $response['result'];

        //I must remember to add names to this one as well
        for($i=0; $i < 5; $i++){
            $pname = nameByID($mysqli,$data[$i]['playerid']);
            echo "$i \t {$data[$i]['playerid']} \t $pname  \t {$data[$i]['goal_kicks']}\n";
        }

    }
    else{
        echo $response['error'];
    }

///////////////////////////////////////////////////////////////////////////////////////////////////////

    $sql = "SELECT `playerid`,AVG(`yards`) AS yardage\n"
        .   "FROM `players_stats`\n"
        .   "WHERE `statid` = 70\n"
        .   "GROUP BY `playerid`\n"
        .   "ORDER BY yardage";

        $response = runQuery($mysqli,$sql);
    
    if($response['success']){
        echo "\n9.) shortest average goal kick length: \n\n";
        echo "# \t id \t\t Name \t\t average yardage\n";
        echo "==================================================\n";
        $data = $response['result'];
        
        for($i=0; $i < 5; $i++){
            $pname = nameByID($mysqli,$data[$i]['playerid']);
            echo "$i \t {$data[$i]['playerid']} \t $pname \t {$data[$i]['yardage']}\n";
        }

    }
    else{
        echo $response['error'];
    }



            
?>

<html>
    <body>
        <br>
        <A href="http://cs2.mwsu.edu/~dmcginn/software_tools/">return</A>
    </body>
</html>