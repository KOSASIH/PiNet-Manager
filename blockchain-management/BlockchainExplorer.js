// BlockchainExplorer.js
import React, { useState, useEffect } from 'eact';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles({
  table: {
    minWidth: 650,
  },
});

function BlockchainExplorer() {
  const classes = useStyles();
  const [blocks, setBlocks] = useState([]);

  useEffect(() => {
    fetch('https://example.com/blocks')
     .then(response => response.json())
     .then(data => setBlocks(data));
  }, []);

  return (
    <Paper>
      <TableContainer component={Paper}>
        <Table className={classes.table} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Block Hash</TableCell>
              <TableCell>Block Number</TableCell>
              <TableCell>Timestamp</TableCell>
              <TableCell>Data</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {blocks.map(block => (
              <TableRow key={block.id}>
                <TableCell component="th" scope="row">
                  {block.hash}
                </TableCell>
                <TableCell>{block.number}</TableCell>
                <TableCell>{block.timestamp}</TableCell>
                <TableCell>{block.data}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Paper>
  );
}

export default BlockchainExplorer;
