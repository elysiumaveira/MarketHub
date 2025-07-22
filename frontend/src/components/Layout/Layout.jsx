import { useState } from 'react'
import { Outlet, useNavigate } from 'react-router-dom'

import { useTheme } from '@mui/material/styles'
import { 
    useMediaQuery,
    AppBar, 
    Toolbar, 
    Box,
    Container,
} from '@mui/material'
import IconButton from '@mui/material/IconButton'
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart'
import NotificationsIcon from '@mui/icons-material/Notifications'
import AddIcon from '@mui/icons-material/Add'

import ResponsiveAppBar from '../ResponsiveAppBar/ResponsiveAppBar'
import SearchBar from '../SearchBar/SearchBar'
import MobileBottomNav from '../MobileBottomNavigation/MobileBottomNav'

export default function Layout() {
    const theme = useTheme()
    const isMobile = useMediaQuery(theme.breakpoints.down('sm'))
    const navigate = useNavigate()  
    const [searchTerm, setSearchTerm] = useState('')
    const handleSearch = (term) => {setSearchTerm(term)}

    if (!isMobile) {return (
        <ResponsiveAppBar />
    )} 

    return (
        <>
            <Container maxWidth="sm" sx={{padding: 0}}>
                <AppBar
                    position='static'
                    elevation={0}
                    sx={{
                        backgroundColor: 'transparent'
                    }}
                >
                    <Toolbar>

                        <SearchBar onSearch={handleSearch} />

                        <IconButton aria-label='ShoppingCart' onClick={()=>navigate('/')}>
                            <ShoppingCartIcon />
                        </IconButton>

                        <IconButton aria-label='Notifications' onClick={()=>navigate('/')}>
                            <NotificationsIcon />
                        </IconButton>

                        <IconButton aria-label='CreateAListing' onClick={()=>navigate('/')}>
                            <AddIcon />
                        </IconButton>

                    </Toolbar>
                </AppBar>
            </Container>
            
            <Box>
                <Outlet />
            </Box>

            <MobileBottomNav />
        </>
    )}