import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';

export default function Body() {
  return (
    <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { m: 2, width: 10000, maxWidth: '95%'}, paddingLeft: '2%'
      }}
      noValidate
      autoComplete="off"
    >
      <div>
        <TextField
          name="content"
          id="standard-multiline-static"
          label="Note Content"
          multiline
          //rows={100}
          defaultValue=""
          variant="standard"
          InputProps={{ style: { width: '100%', textDecoration: 'none'}, disableUnderline: true }}
        />
      </div>
    </Box>
  );
}