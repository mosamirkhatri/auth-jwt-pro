import React from "react";
import { Routes, Route } from "react-router-dom";
// Pages
import LoginPage from "../Pages/Login";

const AppRouter = () => {
  return (
    <Routes>
      {/* <Route path="/" element={<PublicPage />} /> */}
      <Route path="/login" element={<LoginPage />} />
      {/* <Route
            path="/protected"
            element={
              <RequireAuth>
                <ProtectedPage />
              </RequireAuth>
            }
          /> */}
    </Routes>
  );
};

export default AppRouter;
