import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';

export default function Title1() {

    const [title, setTitle] = React.useState('')
  return (
    <Box
      component="form"
      sx={{
        '& > :not(style)': { m: 2, width: '35ch' },paddingLeft: '20%',paddingTop:"5%"
      }}
      noValidate
      autoComplete="off"
    >
      <TextField id="standard-basic" label={title === ""? "Untitled": "Title"} value={title} variant="standard" 
      InputProps={{ sx: {fontSize: '30px',}}}
      
      InputLabelProps={{
        sx: {
          fontSize: '30px',
          
        },
        
        //shrink: false
      }}

      onChange={(e) => setTitle(e.target.value)}
      />
    </Box>
  );
}