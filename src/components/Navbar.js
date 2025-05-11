import React from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
  IconButton,
  Menu,
  MenuItem,
} from '@mui/material';
import {
  AccountCircle,
  SportsEsports,
  School,
  FitnessCenter,
} from '@mui/icons-material';

const Navbar: React.FC = () => {
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const isMenuOpen = Boolean(anchorEl);

  const handleProfileMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography
          variant="h6"
          component={RouterLink}
          to="/"
          sx={{
            flexGrow: 1,
            textDecoration: 'none',
            color: 'inherit',
            display: 'flex',
            alignItems: 'center',
          }}
        >
          Chess Engine
        </Typography>

        <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
          <Button
            color="inherit"
            component={RouterLink}
            to="/game"
            startIcon={<SportsEsports />}
          >
            Play
          </Button>
          <Button
            color="inherit"
            component={RouterLink}
            to="/tutorials"
            startIcon={<School />}
          >
            Tutorials
          </Button>
          <Button
            color="inherit"
            component={RouterLink}
            to="/training"
            startIcon={<FitnessCenter />}
          >
            Training
          </Button>
          <IconButton
            edge="end"
            aria-label="account of current user"
            aria-controls="menu-appbar"
            aria-haspopup="true"
            onClick={handleProfileMenuOpen}
            color="inherit"
          >
            <AccountCircle />
          </IconButton>
        </Box>

        <Menu
          id="menu-appbar"
          anchorEl={anchorEl}
          anchorOrigin={{
            vertical: 'bottom',
            horizontal: 'right',
          }}
          keepMounted
          transformOrigin={{
            vertical: 'top',
            horizontal: 'right',
          }}
          open={isMenuOpen}
          onClose={handleMenuClose}
        >
          <MenuItem
            component={RouterLink}
            to="/profile"
            onClick={handleMenuClose}
          >
            Profile
          </MenuItem>
          <MenuItem
            component={RouterLink}
            to="/login"
            onClick={handleMenuClose}
          >
            Login
          </MenuItem>
          <MenuItem
            component={RouterLink}
            to="/register"
            onClick={handleMenuClose}
          >
            Register
          </MenuItem>
        </Menu>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar; 