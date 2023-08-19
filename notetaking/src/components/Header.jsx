import * as React from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';

const theme = createTheme({
  palette: {
    primary: {
      main: '#373737',
    },
  },
});

export default function Header() {
  return (
    <ThemeProvider theme={theme}>
      <Box classname = "appbar">
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Editing...
            </Typography>
            <Button color="inherit">Confirm Edits</Button>
          </Toolbar>
        </AppBar>
      </Box>
    </ThemeProvider>
  );
}