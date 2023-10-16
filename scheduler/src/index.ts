import { program } from "commander";
import AvailabilityDomainsService from "./service";

const availabilityTask = async () => {
  const service = new AvailabilityDomainsService();
  await service.pingDomains();

  process.exit(0);
};

const snapshotTask = () => {
  console.log("Running snapshot task");
  process.exit(0);
};

(() => {
  program
    .name("Checkstatus Scheduler")
    .description("CLI for the Checkstatus Scheduler");

  program
    .command("ping")
    .description("Run a availability of domain services")
    .action(async () => {
      await availabilityTask();
    });

  program
    .command("snapshot")
    .description("Run a snapshot homepage site domain")
    .action(() => {
      snapshotTask();
    });

  program.parse();
})();
