import React from "react";
import { Routes, Route } from "react-router-dom";
import PrivateRoute from "./PrivateRoute";
// Pages
const LoginPage = React.lazy(() => import("../pages/Login"));
const ProtectedPage = React.lazy(() => import("../pages/Protected"));
const ExplorePage = React.lazy(() => import("../pages/Explore"));

export default function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/protected" element={<PrivateRoute />}>
        <Route path="" element={<ProtectedPage />} />
      </Route>
      <Route path="/explore" element={<PrivateRoute />}>
        <Route path="" element={<ExplorePage />} />
      </Route>
    </Routes>
  );
}
