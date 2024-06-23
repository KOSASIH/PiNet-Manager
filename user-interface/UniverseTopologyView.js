import { TopologyView } from "topology-view";

class UniverseTopologyView extends TopologyView {
  constructor() {
    super();
    this.universeTopology = [];
  }

  addDevice(device) {
    this.universeTopology.push(device);
  }

  addNetworkGroup(networkGroup) {
    this.universeTopology.push(networkGroup);
  }

  render() {
    return this.universeTopology.map((item) => {
      return `<div>${item.name}</div>`;
    }).join("");
  }
}

export default UniverseTopologyView;
