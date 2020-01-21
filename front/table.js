import React from 'react';
import { makeStyles } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";


const useStyles = makeStyles({
  table: {
    minWidth: 650
  }
});

function createData(date, temp2M, tempS, humid, vent, neige) {
  return { date, temp2M, tempS, humid, vent, neige };
}

const rows = [
  createData("Test", 159, 6.0, 24, 4.0, 5),
  createData(159, 6.0, 24, 4.0, 5,'lol')
];

export default function SimpleTable() {
  const classes = useStyles();

  return (
    <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>date</TableCell>
            <TableCell align="right">Temperature à 2m</TableCell>
            <TableCell align="right">Temperature au sol</TableCell>
            <TableCell align="right">Humidité</TableCell>
            <TableCell align="right">Vent moyen</TableCell>
            <TableCell align="right">Risque de neige</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map(row => (
            <TableRow key={row.date}>
              <TableCell component="th" scope="row">
                {row.date}
              </TableCell>
              <TableCell align="right">{row.temp2M}</TableCell>
              <TableCell align="right">{row.tempS}</TableCell>
              <TableCell align="right">{row.humid}</TableCell>
              <TableCell align="right">{row.vent}</TableCell>
              <TableCell align="right">{row.neige}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer> 
  );
}
