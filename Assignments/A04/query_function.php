<?php
/**
 * This function runs a SQL query and returns the data in an associative array
 * that looks like:
 * $response [
 *      "success" => true or false
 *      "error" => contains error if success == false
 *      "result" => associative array of the result
 * ]
 *
 */
function runQuery($mysqli,$sql){
    $response = [];

    // run the query
    $result = $mysqli->query($sql);

    // If we were successful
    if($result){
        $response['success'] = true;
        // loop through the result printing each row
        while($row = $result->fetch_assoc()){
            $response['result'][] = $row;
        }
        $result->free();
    }else{
        $response['success'] = false;
        $response['error'] = $mysqli->error;
    }

    return $response;
}

/*
    This function returns the name of a player based on their ID
    accepts $mysqli and $pid , a player's ID
*/
function nameByID($mysqli,$pid){
    $name;
    $pid = $mysqli -> real_escape_string($pid);
    $sql = "SELECT `name`\n"
        .  "FROM `players`\n"
        .  "WHERE `id` = '$pid'";

    $response = runQuery($mysqli,$sql);

    if($response['success']){
        $data = $response['result'];
        //$name = $pid;
        $name = $data[0]['name'];
    }
    else
    {
        $name = $response['error'];
    }

    return $name;


}