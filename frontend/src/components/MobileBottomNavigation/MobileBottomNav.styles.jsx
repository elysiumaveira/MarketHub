import { styled } from '@mui/material/styles'
import { BottomNavigation } from '@mui/material'

const CustomBottomNavigation = styled(BottomNavigation)(({theme})=>({
    position: 'fixed',
    bottom: 0,
    left: 0,
    right: 0,
    zIndex: 1100,
    backgroundColor: 'background.paper',
    borderTop: '1px solid rgba(0, 0, 0, 0.1)',
    height: 66,
    width: '100%'
}))

export default CustomBottomNavigation