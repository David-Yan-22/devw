import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';

export default function Body() {
    const [body, setBody] = React.useState('')
  return (
    <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { m: 2, width: 10000, maxWidth: '60%'}, paddingLeft: '20%'
      }}
      noValidate
      autoComplete="off"
    >
      <div>
        <TextField
          name="content"
          id="standard-multiline-static"
          label={body === ""? "No Content": "Note Content"}
          value = {body}
          multiline
          //rows={100}
          defaultValue=""
          variant="standard"
          InputProps={{ style: { width: '100%', textDecoration: 'none'}, disableUnderline: true }}

          onChange={(e) => setBody(e.target.value)}
        />
      </div>
      
    </Box>
    
  );
}