// Import From Library
import React from "react";
import { Navigate, Outlet, useLocation } from "react-router-dom";
import { useAuthStore } from "../store/authStore";

export default function PrivateRoute() {
  const location = useLocation();
  // const { isLoggedIn: isAuthenticated } = useAuthStore();
  let isAuthenticated = true;
  return isAuthenticated ? (
    <Outlet />
  ) : (
    <Navigate to={"/login"} state={{ from: location }} />
  );
}
