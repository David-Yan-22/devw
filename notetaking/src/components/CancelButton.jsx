import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Link from 'next/link';

export default function CancelButton() {
  return (
    <Stack direction="row" spacing={2}>
        <Link href="http://localhost:3000/home">
      <Button variant="contained" style={{ backgroundColor: '#F3C4AF', color: 'white' }}>
        Cancel Edits
      </Button>
      </Link>
    </Stack>
  );
}