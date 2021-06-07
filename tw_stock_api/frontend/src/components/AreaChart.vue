<script>
import { Line } from "vue3-chart-v2";
import { useToast } from 'vue-toastification'

const toast = useToast()

export default {
  extends: Line,
  data() {
    return {
      gradient: null,
    };
  },
  mounted() {
    this.$api.auth.getApiUseCount().then(async (response) => {
        const { data } = response;
        console.log(data)

        this.gradient = this.$refs.canvas
          .getContext("2d")
          .createLinearGradient(0, 0, 0, 450);
        this.gradient2 = this.$refs.canvas
          .getContext("2d")
          .createLinearGradient(0, 0, 0, 450);

        this.gradient.addColorStop(0, "rgba(255, 0,0, 0.5)");
        this.gradient.addColorStop(0.5, "rgba(255, 0, 0, 0.25)");
        this.gradient.addColorStop(1, "rgba(255, 0, 0, 0)");
        this.renderChart(
        {
          labels: data.labels,
          datasets: [
            {
              label: "Data One",
              borderColor: "#FC2525",
              pointBackgroundColor: "white",
              borderWidth: 1,
              pointBorderColor: "white",
              backgroundColor: this.gradient,
              data: data.data
            }
          ]
        },
        { responsive: true, maintainAspectRatio: false }
      );
      
    }).catch(() => {
        toast.error('不明錯誤')
    });
    
  }
};
</script>
