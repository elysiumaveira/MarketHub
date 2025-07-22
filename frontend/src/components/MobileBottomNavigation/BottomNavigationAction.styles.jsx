import { styled } from '@mui/material/styles'
import { BottomNavigationAction } from '@mui/material'

const CustomBottomNavigationAction = styled(BottomNavigationAction)(({theme})=>({
    padding: '0px',
    height: '56px',
    width: '86px'
}))

export default CustomBottomNavigationAction