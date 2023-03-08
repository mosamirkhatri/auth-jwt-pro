// Library
import React from "react";
import { Flex } from "@mantine/core";
// Components
import AppHeader from "../AppHeader";
import AppFooter from "../AppFooter";

const PageLayout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <Flex
      sx={{ minHeight: "100vh", ".page-content": { flex: 1 } }}
      direction={"column"}
    >
      <AppHeader />
      {children}
      <AppFooter />
    </Flex>
  );
};

export default PageLayout;
