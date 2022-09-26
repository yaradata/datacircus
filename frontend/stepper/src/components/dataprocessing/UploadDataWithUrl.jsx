import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import { Button } from '@mui/material';


const separators = [
    {
      value: ',',
      label: 'comma (,)'
    },
    {
      value: ';',
      label: 'point comma (;)'
    },
    {
      value: '|',
      label: 'pipe (|)',
    }
]


const UploadDataWithUrl = () => {
    const [separator, setSeparator] = React.useState(',');

    const handleChange = (event) => {
        setSeparator(event.target.value);
    };

    return (
        <div>
            <form>
                <TextField
                id="outlined-select-currency"
                select
                label="Separator"
                value={separator}
                onChange={handleChange}
                helperText="Please select your separator"
                fullWidth
                >
                {separators.map((option) => (
                    <MenuItem key={option.value} value={option.value}>
                    {option.label}
                    </MenuItem>
                ))}
                </TextField>
                
                {/* <TextField id="outlined-basic" label="Url" variant="outlined" /> */}
                <TextField 
                    id="filled-search-train"
                    label="Url train"
                    type="search"
                    variant="filled"
                    fullWidth
                    // onBlur={ e => uploadWithUrl(e) }
                />

                <Button variant="contained">Submit</Button>

            </form>
        </div>
    );
}


export default UploadDataWithUrl;
