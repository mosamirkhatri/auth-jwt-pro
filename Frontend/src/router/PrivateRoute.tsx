// Import From Library
import React from "react";
import { Navigate, Outlet, useLocation } from "react-router-dom";

export default function PrivateRoute() {
  const location = useLocation();
  let isAuthenticated = true;
  return isAuthenticated ? (
    <Outlet />
  ) : (
    <Navigate to={"/login"} state={{ from: location }} />
  );
}
