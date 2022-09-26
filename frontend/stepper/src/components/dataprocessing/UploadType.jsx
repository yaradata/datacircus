import { Switch } from '@mui/material';
import React from 'react';

function UploadType(props) {
    return (
        <div>
            <span>browser</span>
            <Switch
            // checked={checked}
            // onChange={handleChange}
            inputProps={{ 'aria-label': 'controlled' }}
            />
            <span>url</span>
        </div>
    );
}

export default UploadType;