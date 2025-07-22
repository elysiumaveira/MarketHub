import * as React from 'react'

import Button from '@mui/material/Button'
import AddIcon from '@mui/icons-material/Add'
import ColorButton from './ColorButton.styles'

export default function CreateButton() {
    return (
        <ColorButton
            startIcon={<AddIcon />}
            variant="contained"
            sx={{ my: 2 }}
        >
            Подать объявление
        </ColorButton>
    )
}