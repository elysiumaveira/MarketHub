import Button from '@mui/material/Button'
import { styled } from '@mui/material/styles'
import { blue } from '@mui/material/colors'

const ColorButton = styled(Button)(({theme}) => ({
    color: theme.palette.getContrastText(blue[500]),
    backgroundColor: blue[500],
    '&:hover': {
        backgroundColor: blue[700],
    },
    textTransform: "none",
}))

export default ColorButton