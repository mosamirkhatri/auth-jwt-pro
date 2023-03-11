import { Box } from "@mantine/core";
import AuthForm from "../../components/login/AuthForm";
import PageLayout from "../../components/shared/PageLayout";
// Styles
import { useStyles } from "./LoginPage.styles";

const LoginPage = () => {
  const { classes } = useStyles();
  return (
    <PageLayout>
      <Box className={`page-content ${classes["page-content"]}`}>
        <AuthForm mx={"xs"} sx={{ minWidth: "25%" }} />
      </Box>
    </PageLayout>
  );
};

export default LoginPage;
