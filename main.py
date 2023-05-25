<!DOCTYPE html>
<html>
<head>
    <title>Wi-Fi Status</title>
    <style>
        head {
            display: none;
        }
        body {
            font-family: sans-serif;
            margin: 0 auto;
            padding: 1em;
            background-color: #282828;
            color: #ebdbb2;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        h1 {
            margin-bottom: 1em;
        }

        form {
            margin-bottom: 1em;
        }
        
        label {
            display: block;
            margin-bottom: 0.5em;
            color: #ebdbb2;
        }
        
        input[type="number"] {
            padding: 0.5em;
            border-radius: 4px;
            border: 1px solid #ebdbb2;
            background-color: #282828;
            color: #ebdbb2;
        }
        
        input[type="submit"] {
            padding: 0.5em 1em;
            border-radius: 4px;
            border: none;
            background-color: #ebdbb2;
            color: #282828;
            cursor: pointer;
        }
        button {
            padding: 0.5em 1em;
            border-radius: 4px;
            border: none;
            background-color: #ebdbb2;
            color: #282828;
            cursor: pointer;
        }
        
        h2 {
            margin-bottom: 0.5em;
        }
        
        table {
            width: 95vw;
            border-collapse: collapse;
        }
        
        th, td {
            padding: 0.5em;
            border: 1px solid #ebdbb2;
        }

        #inputCntr {
            display: flex;
            flex-direction: row;
            justify-content: space-evenly;
            align-items: last baseline;
            width: 100%;
        }
    </style>
</head>
<body>
    <h1>Wi-Fi Status Detector and Logger</h1>
    <div id="inputCntr">
        <div>
            <form method="POST">
                <label for="refresh_rate">Refresh Rate (seconds):</label>
                <input type="number" id="refresh_rate" name="refresh_rate" min="1" max="60" value="%s">
                <input type="submit" value="Set">
            </form>
        </div>
        <div>
            <form action="POST">

            </form>
        </div>
        <div>
            <form action="POST">
                <button type="submit">
                    Download Log
                </button>
                <button type="submit">
                    Clear Log
                </button>
            </form>
        </div>
    </div>
    <h2>Status Log</h2>
    <table>
        <tr>
            <th>Date/Time</th>
            <th>Status</th>
        </tr>
        %s
    </table>
</body>
</html>
