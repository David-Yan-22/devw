import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Link from 'next/link';

export default function SubmitButton() {
  return (
    <Stack direction="row" spacing={2}>
        <Link href="http://localhost:3000/home">
      <Button variant="contained" style={{ backgroundColor: '#A2DBC5', color: 'white' }}>
        Confirm Edits
      </Button>
      </Link>
      
    </Stack>
  );
}