import * as React from 'react'

import SearchBar from '../SearchBar/SearchBar'
import CategoriesMenu from './CategoriesMenu'
import UserMenu from './UserMenu'
import CreateButton from './CreateButton'

import AppBar from '@mui/material/AppBar'
import Box from '@mui/material/Box'
import Toolbar from '@mui/material/Toolbar'
import Typography from '@mui/material/Typography'
import Container from '@mui/material/Container'

const settings = ['Profile', 'Account', 'Dashboard', 'Logout']

export default function ResponsiveAppBar() {
    const [anchorElNav, setAnchorElNav] = React.useState(null)
    const [anchorElUser, setAnchorElUser] = React.useState(null)

    const handleOpenNavMenu = (event) => {
        setAnchorElNav(event.currentTarget)
    }

    const handleOpenUserMenu = (event) => {
        setAnchorElUser(event.currentTarget)
    }

    const handleCloseNavMenu = () => {
        setAnchorElNav(null);
    }

    const handleCloseUserMenu = () => {
        setAnchorElUser(null);
    }

    return (
        <AppBar position="static">
            <Container maxWidth="xl">
                <Toolbar disableGutters>

                    <Typography
                        variant="h6"
                        noWrap
                        component="a"
                        href="/"
                        sx={{
                        mr: 2,
                        display: { xs: 'none', md: 'flex' },
                            fontFamily: 'monospace',
                            fontWeight: 700,
                            letterSpacing: '.3rem',
                            color: 'inherit',
                            textDecoration: 'none',
                        }}
                    >
                        MarketHub
                    </Typography>
                    
                    <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
                        <CategoriesMenu />

                        <Container sx={{ my: 2 }}>
                            <SearchBar />
                        </Container>

                    </Box>
                    
                    <Box sx={{ flexGrow: .05 }}>
                        <CreateButton />
                    </Box>

                    <Box sx={{ flexGrow: 0 }} >
                        <UserMenu />
                    </Box>

                </Toolbar>
            </Container>
        </AppBar>
    )
}