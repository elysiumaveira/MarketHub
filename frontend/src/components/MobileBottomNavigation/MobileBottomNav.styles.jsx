import { styled } from '@mui/material/styles'
import { BottomNavigation } from '@mui/material'

const CustomBottomNavigation = styled(BottomNavigation)(({theme})=>({
    position: 'fixed',
    bottom: '0px',
    left: '0px',
    right: '0px',
    zIndex: 1100,
    backgroundColor: 'background.paper',
    borderTop: '1px solid rgba(0, 0, 0, 0.1)',
    height: '66px',
    width: '100%'
}))

export default CustomBottomNavigation