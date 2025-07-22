import * as React from 'react'

import ColorButton from './ColorButton.styles'

import Menu from '@mui/material/Menu'
import MenuItem from '@mui/material/MenuItem'
import MenuIcon from '@mui/icons-material/Menu'

export default function CategoriesMenu() {
  const [anchorEl, setAnchorEl] = React.useState(null)
  const open = Boolean(anchorEl)
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget)
  }
  const handleClose = () => {
    setAnchorEl(null)
  }

  return (
    <div>
      <ColorButton
          id="categories-menu"
          aria-controls={open ? 'categories-menu' : undefined}
          aria-haspopup="true"
          aria-expanded={open ? 'true' : undefined}
          onClick={handleClick}
          variant="contained"
          startIcon={<MenuIcon />}
          sx={{ my: 2, color: 'white' }}
      >
          Категории
      </ColorButton>
      <Menu
        id="categories-menu"
        aria-labelledby="categories-menu"
        anchorEl={anchorEl}
        open={open}
        onClose={handleClose}
        anchorOrigin={{
          vertical: 'top',
          horizontal: 'left',
        }}
        transformOrigin={{
          vertical: 'top',
          horizontal: 'left',
        }}
      >
        <MenuItem onClick={handleClose}>Недвижимость</MenuItem>
        <MenuItem onClick={handleClose}>Мебель</MenuItem>
        <MenuItem onClick={handleClose}>Автомобили</MenuItem>
      </Menu>
    </div>
  )
}